import sys

import typer
import click_spinner
from tabulate import tabulate

from utils import get_networks, get_wifi_port, run_cmd
from constants import TURN_WIFI_ON, TURN_WIFI_OFF, CONNECT_TO_NETWORK

app = typer.Typer(help="CLI wifi manager.")


@app.command()
def list():
    """
    List available networks.
    """
    headers, networks = get_networks()
    typer.echo(tabulate(networks, headers, tablefmt="grid"))


@app.command()
def conn(ssid: str = '', password: str = ''):
    """
    Connect to a wifi network.
    """
    wifi_port = get_wifi_port()
    if not ssid:
        headers, networks = get_networks()
        typer.echo(tabulate(networks, headers, tablefmt="grid"))

        input_ssid = int(typer.prompt("SSID"))
        if input_ssid not in range(1, len(networks) + 1):
            typer.echo('Invalid option.')
            sys.exit()

        ssid = networks[input_ssid - 1][1]

    if not password:
        password = typer.prompt("Password", hide_input=True)

    with click_spinner.spinner():
        typer.echo(f"Connecting to {ssid}.")
        output = run_cmd(CONNECT_TO_NETWORK.format(port=wifi_port, ssid=ssid, password=password))
        if not output:
            typer.echo("Connected to wifi.")
        else:
            typer.echo("Wrong ssid or password.")


@app.command()
def on():
    """
    Turn wifi on.
    """
    with click_spinner.spinner():
        wifi_port = get_wifi_port()
        run_cmd(TURN_WIFI_ON.format(port=wifi_port))
        typer.echo("Wifi is on.")


@app.command()
def off():
    """
    Turn wifi off.
    """
    with click_spinner.spinner():
        wifi_port = get_wifi_port()
        run_cmd(TURN_WIFI_OFF.format(port=wifi_port))
        typer.echo("Wifi is off.")


if __name__ == "__main__":
    app()
