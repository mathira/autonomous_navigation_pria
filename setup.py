from glob import glob
import os

from setuptools import find_packages, setup


package_name = "autonomous_navigation_pria"


setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join(package_name, "launch", "*.launch.py")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="autonomous_navigation_pria maintainers",
    maintainer_email="maintainer@example.com",
    description="PID goal navigation for Stage simulations.",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "pid_navigator = autonomous_navigation_pria.pid_navigator:main",
        ],
    },
)
