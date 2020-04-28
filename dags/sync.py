import time
import airflow.utils.dates
from airflow.operators.bash_operator import BashOperator
from airflow.exceptions import AirflowSkipException
from airflow.models import DAG

# ----------------------------------------------------
dag_name = 'git_sync_dags'

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1)
}

dag = DAG(
    dag_id=dag_name,
    default_args=args,
    schedule_interval='1/2 * * * *'
)


git_sync_dags = BashOperator(
    task_id='git_sync_dags',
	bash_command="git pull https://github.com/LvXinPeng/airflow-sync-dags.git; cp /usr/local/airflow/airflow-sync-dags/*.py /usr/local/airflow/dags/",
    dag=dag)
end = BashOperator(
    task_id='end',
	bash_command="echo end ... ...",
    dag=dag)


git_sync_dags >> end



# ----------------------------------------------------
if __name__ == "__main__":
    pass