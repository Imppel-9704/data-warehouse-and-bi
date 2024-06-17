import logging

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def _hello_world():
    logging.debug('This is debug log')
    logging.info('hello world!')


# Parameters will be writter.
# required 3 parameters 1.dag_id 2.start_date 3.schedule
# dag_id should be the same name as file for easy debugging
# schedule is None means DAG will be trigger when we run trigger button
with DAG(
    dag_id= "hello",
    start_date= timezone.datetime(2024, 6, 12),
    schedule= None,
    tags= ['dw-and-bi'],
):

    # task_id should be named same as what the task do
    start = EmptyOperator(task_id= 'start')

    echo_hello = BashOperator(
        task_id= 'echo_hello',
        bash_command= "echo 'hello'",
        )

    hello_world = PythonOperator(
        task_id= 'hello_world',
        python_callable= _hello_world
    )

    end = EmptyOperator(task_id= 'end')

    start >> echo_hello >> end
    start >> hello_world >> end