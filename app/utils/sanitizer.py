import bleach

def sanitize_input(input_data: str) -> str:
    """Cleans HTML/JS from form inputs."""
    return bleach.clean(input_data)
