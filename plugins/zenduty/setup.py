from setuptools import find_packages, setup

version = "5.3.1"

setup(
    name="alerta-zenduty",
    version=version,
    description="Alerta plugin for zenduty",
    url="https://github.com/Zenduty/alerta-contrib",
    license="MIT",
    author="Zenduty",
    author_email="contact@zenduty.com",
    packages=find_packages(),
    py_modules=["zenduty"],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=True,
    entry_points={"alerta.plugins": ["zenduty = zenduty:TriggerEvent"]},
)
