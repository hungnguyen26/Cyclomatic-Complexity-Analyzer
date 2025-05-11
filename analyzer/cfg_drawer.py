import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

def draw_cfg(edges):
    if not edges:
        st.info("Không có dữ liệu CFG.")
        return

    G = nx.DiGraph()
    for src, dst in edges:
        G.add_edge(src, dst)

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=1500,
            node_color="lightgreen", ax=ax)
    st.pyplot(fig)
