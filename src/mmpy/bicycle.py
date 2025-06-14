from pathlib import Path
import typing as tp
import networkx as nx
def construct_graph(
        availability_by_musician: tp.Dict[str,tp.Dict[str,bool]],
        instruments_by_musician: tp.Dict[str,tp.List],
    )-> nx.Graph:
    """
    Creates the constraint graph
    """
    return nx.Graph()

def match( 
        cg: nx.Graph
    ) -> tp.Dict:
    """
    Computes a list of assignments in increasing order of severity of problems or cost 
    Args:
        : cg the constraint graph 
    """
    dp = Path(__file__).parent.joinpath('data.txt')
    #from IPyhton import embed;embed()
    return [
        {
            "05.04.2026": {
                "Markus":"Bass",
                "Sandro":"Drum set",
                "Luisa" :"Gesang"
            },
            "12.04.2026": {
                "Johannes":"Piano",
                "Moritz":"Cachon",
                "Feli" :"Gesang"
            },
            "19.04.2026": {
                "Johannes":"Piano",
                "Moritz":"Cachon",
                "Feli" :"Gesang"
            },
            "26.04.2026": {
                "Moritz":"Gitarre",
                "Sarah" :"Gesang",
                "Sara" :"Geige"
            }
        }
    ]



