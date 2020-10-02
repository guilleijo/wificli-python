import sys
import subprocess

import typer
import click_spinner

from constants import LIST_CMD, IS_WIFI_OFF, GET_WIFI_PORT


def run_cmd(cmd: str):
    out = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    return out.stdout.decode('utf-8')


def get_networks():
    typer.echo('Getting networks list')
    with click_spinner.spinner():
        output = run_cmd(LIST_CMD)
        if not output:
            msg = (
                'It looks like the wifi is off. You can turn it on running `wificli on`.'
                if _is_wifi_off()
                else 'Wifi is turning on, try again in a couple of seconds.'
            )
            typer.echo(msg)
            sys.exit()

        wifi_list = [
            [i, w.strip().split()[0]]
            for i, w in enumerate(output.split('\n')[:-1])
        ]

        headers = ["SSID"]
        networks = wifi_list[1:]

    return headers, networks


def get_wifi_port():
    output = run_cmd(GET_WIFI_PORT)
    port = output.split('Wi-Fi')[1].split('\n')[1].split(' ')[1]
    return port


def _is_wifi_off():
    with click_spinner.spinner():
        output = run_cmd(IS_WIFI_OFF)
        return output == "AirPort: Off\n"
