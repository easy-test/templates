#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-10 23:50:15
# @Author  : zzz {easy-quest@vk.com}
# @Link    : https://github.com/easy-quest/
# @Version : 1.0.0

import os
import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
def cli():
    click.launch('https://click.palletsprojects.com/')
    pass



click.echo(click.style('Hello World!', fg='green'))
click.echo(click.style('ATTENTION!', blink=True))
click.echo(click.style('Some things', reverse=True, fg='cyan'))
click.echo(click.style('More colors', fg=(255, 12, 128), bg=117))
click.secho('Hello World!', fg='green')
click.echo(click.style('Hello World!', fg='green'))
