import click

# from sidewalk_gaps.db_setup import commands as db_setup_commands
from sidewalk_gaps.accessibility import commands as accessibility_commands
from sidewalk_gaps.segments import commands as segment_commands
from sidewalk_gaps.data_viz import commands as viz_commands
from sidewalk_gaps.extract_data import commands as extraction_commands

from helpers import db_connection, generate_nodes


@click.group()
def main():
    "The command 'sidewalk' is used for the Sidewalk Gap Analysis project."
    pass


@click.command()
def make_nodes():
    """ Generate topologically-sound nodes for the sidewalk lines """

    db = db_connection()

    kwargs = {
        "new_table_name": "nodes_for_sidewalks",
        "geom_type": "Point",
        "epsg": 26918,
        "uid_col": "sw_node_id",
    }

    generate_nodes(db, "pedestriannetwork_lines", "public", kwargs)


all_commands = [
    make_nodes,
    extraction_commands.clip_data,
    accessibility_commands.analyze_network,
    segment_commands.analyze_segments,
    segment_commands.identify_islands,
    viz_commands.combine_centerlines,
]

for cmd in all_commands:
    main.add_command(cmd)


# main.add_command(viz_commands.summarize_into_hexagons)
# main.add_command(viz_commands.classify_hexagons)
