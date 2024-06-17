from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator

# Parameters will be writter.
# required 3 parameters 1.dag_id 2.start_date 3.schedule
# dag_id should be the same name as file for easy debugging
# schedule is None means DAG will be trigger when we run trigger button
with DAG(
    dag_id= "my_first_dag",
    start_date= timezone.datetime(2024, 6, 12),
    schedule= None,
    tags= ['dw-and-bi'],
):

    # task_id should be named same as what the task do
    my_first_task = EmptyOperator(task_id= 'my_first_task')
    my_second_task = EmptyOperator(task_id= 'my_second_task')

    my_first_task >> my_second_task