import argparse

from model import Status, Mode, Employee, Student, Robot
import logging

if __name__ == "__main__":
    log: logging.Logger = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())

    # Get mode argument from command line
    parser = argparse.ArgumentParser(description="Get mode argument from command line")
    parser.add_argument("mode", help="mode argument", type=Mode)
    args = parser.parse_args()

    # Create instance of Employee, Student or Robot based on mode argument. The
    # properties for each object will be loaded from the environment.
    match args.mode:
        case Mode.EMPLOYEE:
            employee = Employee()  # type: ignore
            employee.status = Status.SUCCESSFUL
            log.info(employee)
        case Mode.STUDENT:
            student = Student()  # type: ignore
            student.status = Status.SUCCESSFUL
            log.info(student)
        case Mode.ROBOT:
            robot = Robot()  # type: ignore
            robot.status = Status.SUCCESSFUL
            log.info(robot)
