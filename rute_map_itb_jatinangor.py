import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

data_jarak = [
    ("LABTER", "GKU 2", 90),
    ("GKU 2", "GKU 1", 80),
    ("GKU 1", "Gedung D", 30),
    ("GKU 1", "Gedung E", 30),
    ("GKU 1", "Gedung Rektorat", 200),
    ("Gedung D", "Gedung Rektorat", 110),
    ("Gerbang", "Parkiran", 340),
    ("Gerbang", "GKU 2", 500),
    ("Gerbang", "LABTEK 1 B", 560),
    ("GKU 2", "LABTEK 1 B", 30),
    ("LABTEK 1 A", "LABTEK 1 B", 80),
    ("LABTEK 1 A", "Al-Wasath", 100),
    ("Al-Wasath", "GKU 2", 200),
    ("LABTEK 1 A", "TB 5", 40),
    ("Gedung D", "Al-Wasath", 60),
    ("Gedung E", "Al-Wasath", 60),
    ("Al-Wasath", "Gedung C", 40),
    ("Al-Wasath", "Gedung A", 50),
    ("Al-Wasath", "Gedung B", 60),
    ("Al-Wasath", "Kantin KOICA", 130),
    ("KOICA", "Kantin KOICA", 10),
    ("KOICA", "Gedung Rektorat", 60),
    ("KOICA", "GKU 3", 70),
    ("GKU 3", "Gedung Rektorat", 130),
    ("Gedung B", "TB 4", 60),
    ("TB 1", "TB 2", 30),
    ("TB 2", "TB 3", 30),
    ("TB 3", "TB 4", 30),
    ("TB 1", "GOR Futsal", 20),
    ("Gedung B", "Amphitheater", 110),
    ("TB 5", "SITH", 90),
    ("Amphitheater", "GSG", 160),
    ("GOR Futsal", "GSG", 60),
    ("Amphitheater", "Gedung A", 90),
    ("TB 1", "GOR Tennis Meja", 120),
    ("KOICA", "Lapangan Basket", 130),
    ("Parkiran", "LABTEK 1 B", 175),
    ("GOR Futsal", "GOR Tennis Meja", 80),
    ("SITH", "Gedung B", 50),
    ("SITH", "TB 4", 50),
    ("TB 1", "Lapangan Bola", 80),
    ("TB 2", "Lapangan Bola", 50),
    ("TB 3", "Lapangan Bola", 20),
    ("TB 4", "Lapangan Bola", 40),
    ("GOR Tennis Meja", "Lapangan Bola", 140),
    ("Parkiran", "GKU 2", 160),
    ("GKU 3", "Lapangan Basket", 60),
    ("GSG", "Lapangan Basket", 30),
    ("LABTER", "GKU 1", 40),
    ("Gedung D", "Gedung E", 10),
]

for a, b, jarak in data_jarak:
  G.add_edge(a, b, weight=jarak)

daftar_ruangan = {
    # GEDUNG A
    "A.1.9601": {"building": "Gedung A", "floor": 1},
    "A.1.9602": {"building": "Gedung A", "floor": 1},
    "A.1.9603": {"building": "Gedung A", "floor": 1},
    "A.1.9604": {"building": "Gedung A", "floor": 1},
    "A.1.9605": {"building": "Gedung A", "floor": 1},
    "A.1.9606": {"building": "Gedung A", "floor": 1},
    "A.2.9607/08": {"building": "Gedung A", "floor": 2},
    "A.2.9609/10": {"building": "Gedung A", "floor": 2},
    "A.2.9611/12": {"building": "Gedung A", "floor": 2},
    # GEDUNG B
    "B1.9617": {"building": "Gedung B", "floor": 1},
    "B1.9618": {"building": "Gedung B", "floor": 1},
    "B2.9621": {"building": "Gedung B", "floor": 1},
    "B1.9622": {"building": "Gedung B", "floor": 1},
    # GEDUNG C
    "Lab Fisika 2": {"building": "Gedung C", "floor": 1},
    "Studio A": {"building": "Gedung C", "floor": 1},
    "Studio B": {"building": "Gedung C", "floor": 2},
    # GEDUNG D
    "D1.9633/34": {"building": "Gedung D", "floor": 1},
    "D1.9635": {"building": "Gedung D", "floor": 1},
    "D1.9636": {"building": "Gedung D", "floor": 1},
    "D2.9639": {"building": "Gedung D", "floor": 2},
    "D2.9640": {"building": "Gedung D", "floor": 2},
    "D2.9641": {"building": "Gedung D", "floor": 2},
    "D2.9642": {"building": "Gedung D", "floor": 2},
    # GEDUNG E
    "E1.9646": {"building": "Gedung E", "floor": 1},
    "E1.9647/48": {"building": "Gedung E", "floor": 1},
    "E2.9649": {"building": "Gedung E", "floor": 2},
    "E2.9652": {"building": "Gedung E", "floor": 2},
    # GKU 1
    "K1.9675": {"building": "GKU 1", "floor": 3},
    "K1.9676": {"building": "GKU 1", "floor": 3},
    "K1.9677": {"building": "GKU 1", "floor": 3},
    "K1.9678": {"building": "GKU 1", "floor": 3},
    "K1.9679a": {"building": "GKU 1", "floor": 4},
    "K1.9679b": {"building": "GKU 1", "floor": 4},
    "K1.9680a": {"building": "GKU 1", "floor": 4},
    "K1.9680b": {"building": "GKU 1", "floor": 4},
    "Student Lounge": {"building": "GKU 1", "floor": 2},
    # GKU 2
    "K2.9653": {"building": "GKU 2", "floor": 3},
    "K2.9654": {"building": "GKU 2", "floor": 3},
    "K2.9655": {"building": "GKU 2", "floor": 3},
    "K2.9656": {"building": "GKU 2", "floor": 3},
    "K2.9657": {"building": "GKU 2", "floor": 3},
    "Indomaret": {"building": "GKU 2", "floor": 2},
    # GKU 3
    "K3.101": {"building": "GKU 3", "floor": 1},
    "K3.102": {"building": "GKU 3", "floor": 1},
    "K3.201": {"building": "GKU 3", "floor": 2},
    "K3.202": {"building": "GKU 3", "floor": 2},
    "K3.203": {"building": "GKU 3", "floor": 2},
    "K3.204": {"building": "GKU 3", "floor": 2},
    "K3.301": {"building": "GKU 3", "floor": 3},
    "K3.302": {"building": "GKU 3", "floor": 3},
    "K3.303": {"building": "GKU 3", "floor": 3},
    "K3.304": {"building": "GKU 3", "floor": 3},
    # LABTEK 1-A
    "LTD.9658": {"building": "LABTEK 1 A", "floor": 1},
    "LTD.9659": {"building": "LABTEK 1 A", "floor": 1},
    "LTD.9660": {"building": "LABTEK 1 A", "floor": 1},
    "LTD.9661": {"building": "LABTEK 1 A", "floor": 1},
    "Lt1.012/Lab. Kimia": {"building": "LABTEK 1 A", "floor": 2},
    "Ltd 1 138": {"building": "LABTEK 1 A", "floor": 2},
    "Ltd.II.015": {"building": "LABTEK 1 A", "floor": 3},
    "Ltd.II.9662": {"building": "LABTEK 1 A", "floor": 3},
    "Ltd.II.019": {"building": "LABTEK 1 A", "floor": 3},
    "Lt. II.024/Lab. Fisika": {"building": "LABTEK 1 A", "floor": 3},
    "Lt. II 007": {"building": "LABTEK 1 A", "floor": 3},
    "Lt. III.010/ Lab. Kimia": {"building": "LABTEK 1 A", "floor": 4},
    "Lt. III.023": {"building": "LABTEK 1 A", "floor": 4},
    "Lt. III.025": {"building": "LABTEK 1 A", "floor": 4},
    "Lt. III.033": {"building": "LABTEK 1 A", "floor": 4},
    "Lt. III.041": {"building": "LABTEK 1 A", "floor": 4},
    "Lt. III.043": {"building": "LABTEK 1 A", "floor": 4},
    # LABTEK 1-B
    "L1b.d.9664": {"building": "LABTEK 1 B", "floor": 1},
    "L1b.18": {"building": "LABTEK 1 B", "floor": 1},
    "Lt.B1.04": {"building": "LABTEK 1 B", "floor": 1},
    "R.9667": {"building": "LABTEK 1 B", "floor": 2},
    "R.9668": {"building": "LABTEK 1 B", "floor": 2},
    "R.9669": {"building": "LABTEK 1 B", "floor": 2},
    "R.9670": {"building": "LABTEK 1 B", "floor": 2},
    "R.9671": {"building": "LABTEK 1 B", "floor": 3},
    "R.9672": {"building": "LABTEK 1 B", "floor": 3},
    "R.9673": {"building": "LABTEK 1 B", "floor": 3},
    "R.9674": {"building": "LABTEK 1 B", "floor": 3},
    # GEDUNG KOICA
    "Multipupose": {"building": "KOICA", "floor": 1},
    "Lecter 1": {"building": "KOICA", "floor": 2},
    "Lecter 2": {"building": "KOICA", "floor": 2},
    "Lecter 3": {"building": "KOICA", "floor": 2},
    "Lecter 4": {"building": "KOICA", "floor": 2},
    # GEDUNG UTAMA (Gedung Rektorat)
    "U 101": {"building": "Gedung Rektorat", "floor": 1},
    "U 110": {"building": "Gedung Rektorat", "floor": 1},
    "U 111": {"building": "Gedung Rektorat", "floor": 1},
    "U 202": {"building": "Gedung Rektorat", "floor": 2},
    "U 301": {"building": "Gedung Rektorat", "floor": 3},
    "U 304": {"building": "Gedung Rektorat", "floor": 3},
    "U 305": {"building": "Gedung Rektorat", "floor": 3},
    "U 307": {"building": "Gedung Rektorat", "floor": 3},
    "U 315": {"building": "Gedung Rektorat", "floor": 3},
    "U 316": {"building": "Gedung Rektorat", "floor": 3},
    # DLL
    "GF 1": {"building": "GOR Futsal", "floor": 1},
    "GTM 1": {"building": "GOR Tennis Meja", "floor": 1},
    "GSG": {"building": "GSG", "floor": 1},
    "TB 1": {"building": "TB 1", "floor": 1},
    "TB 2": {"building": "TB 2", "floor": 1},
    "TB 3": {"building": "TB 3", "floor": 1},
    "TB 4": {"building": "TB 4", "floor": 1},
    "Amphitheater": {"building": "Amphitheater", "floor": 1},
    "Gerbang": {"building": "Gerbang", "floor": 1},
    "Parkiran": {"building": "Parkiran", "floor": 1},

}

print("--- SISTEM NAVIGASI KAMPUS ITB JATINANGOR ---")
ruangan_asal = input("Masukkan ruangan asal: ").strip()
ruangan_tujuan = input("Masukkan ruangan tujuan: ").strip()

if ruangan_asal not in daftar_ruangan:
   raise KeyError(f"Ruangan '{ruangan_asal}' tidak ada di daftar ruangan.")
if ruangan_tujuan not in daftar_ruangan:
    raise KeyError(f"Ruangan '{ruangan_tujuan}' tidak ada di daftar ruangan.")

bangunan_asal  = daftar_ruangan[ruangan_asal]["building"]
bangunan_tujuan = daftar_ruangan[ruangan_tujuan]["building"]

print(f"\n[Info] {ruangan_asal} ada di {bangunan_asal}")
print(f"[Info] {ruangan_tujuan} ada di {bangunan_tujuan}")

rute_terbaik = nx.shortest_path(G, source=bangunan_asal, target=bangunan_tujuan, weight='weight')

print("\n--- Rute Terbaik Ditemukan ---")
print(
    f"Dari ruangan: {ruangan_asal} ({bangunan_asal})"
    f" -> Ke ruangan: {ruangan_tujuan} ({bangunan_tujuan})"
  )
print("Rute terbaik:", " -> ".join(rute_terbaik))

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=500, node_color="skyblue")
nx.draw_networkx_edges(G, pos, width=1.5, edge_color="lightgray")
nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold")


path_edges = list(zip(rute_terbaik[:-1], rute_terbaik[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3.5, edge_color="red")
nx.draw_networkx_nodes(
    G, pos, nodelist=rute_terbaik, node_size=600, node_color="springgreen"
)

plt.title(f"Route: {ruangan_asal} ({bangunan_asal}) to {ruangan_tujuan}", fontsize=11)
plt.axis("off")
plt.show()