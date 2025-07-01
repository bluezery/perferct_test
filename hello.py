from prefect import flow


@flow
def hello_world(name: str):
    print(f"Hello, {name}!")
