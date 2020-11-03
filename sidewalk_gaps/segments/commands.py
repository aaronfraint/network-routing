import click

from helpers import db_connection
from .centerline_sidewalk_coverage import classify_centerlines
from .generate_islands import generate_islands


@click.command()
@click.argument("schema")
def analyze_segments(schema: str):
    """ Classify centerlines w/ length of parallel sidewalks """

    db = db_connection()

    classify_centerlines(db, schema, "osm_edges")


@click.command()
@click.argument("schema")
def identify_islands(schema: str, database):
    """ Join intersecting sidewalks to create 'islands' """

    db = db_connection()

    generate_islands(db, schema)
