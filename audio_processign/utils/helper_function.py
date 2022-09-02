import datetime


def get_current_time():
	fmt = "%Y-%m-%d%H-%M-%S"
	return f"{datetime.datetime.now().strftime(fmt)}"
#fmt = "%Y-%m-%d %H%M%S"
#return f"{datetime.now().strftime(fmt)}"
