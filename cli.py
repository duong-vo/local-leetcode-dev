import click


@click.group()
def cli():
    pass

@cli.command('test')
def test():
    print('hey there')



if __name__=='__main__':
    cli()
