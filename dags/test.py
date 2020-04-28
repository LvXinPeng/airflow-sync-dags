import time
import airflow.utils.dates
from airflow.operators.bash_operator import BashOperator
from airflow.exceptions import AirflowSkipException
from airflow.models import DAG

# ----------------------------------------------------
dag_name = 'test'

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1)
}

dag = DAG(
    dag_id=dag_name,
    default_args=args,
    schedule_interval='0 16 * * *'
)


start = BashOperator(
    task_id='start',
	bash_command="echo start... ...",
    dag=dag)
end = BashOperator(
    task_id='end',
	bash_command="echo end ... ...",
    dag=dag)

ETL = BashOperator(
    task_id="ETL",
	bash_command="echo ... ...",
    dag=dag)

phone_number = BashOperator(
    task_id="phone_number",
	bash_command="echo ... ...",
    dag=dag)
name = BashOperator(
    task_id="name",
	bash_command="sleep 3",
    dag=dag)


start >> ETL >> phone_number >> name >>  end



# ----------------------------------------------------
if __name__ == "__main__":
    pass