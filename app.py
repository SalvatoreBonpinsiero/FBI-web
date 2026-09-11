from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
import os

app = Flask(__name__)
REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

VALID_TYPES = {"domain", "ip", "email", "phone", "person", "username", "org", "url", "other"}


def build_graph(target, nodes, links):
    graph = {
        "target": target,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "author": "SalvatoreBonpinsiero",
        "nodes": [],
        "links": [],
    }

    graph["nodes"].append({"id": "__TARGET__", "label": target, "type": "target"})

    for n in nodes:
        value = (n.get("value") or "").strip()
        if not value:
            continue
        ntype = (n.get("type") or "other").lower()
        if ntype not in VALID_TYPES:
            ntype = "other"
        graph["nodes"].append({"id": f"{ntype}:{value}", "label": value, "type": ntype})

    for l in links:
        s = (l.get("source") or "").strip()
        t = (l.get("target") or "").strip()
        if s and t:
            graph["links"].append({"source": s, "target": t})

    return graph


def graph_to_txt(graph):
    line = "=" * 66
    thin = "-" * 66
    out = [
        line,
        "  FBI-WEB // OSINT REPORT",
        "  Developer: SalvatoreBonpinsiero",
        line,
        f"  TARGET       : {graph['target']}",
        f"  DATE         : {graph['created']}",
        f"  NODES        : {len(graph['nodes'])}",
        f"  LINKS        : {len(graph['links'])}",
        thin,
        "  NODES:",
        thin,
    ]

    for n in graph["nodes"]:
        tag = n["type"].upper()
        out.append(f"  [{tag:<8}] {n['label']}")

    out.append("")
    out.append(thin)
    out.append("  LINKS:")
    out.append(thin)

    id2label = {n["id"]: n["label"] for n in graph["nodes"]}
    for l in graph["links"]:
        out.append(f"  {id2label.get(l['source'], l['source'])}  ->  {id2label.get(l['target'], l['target'])}")

    out.append("")
    out.append(line)
    out.append("  END OF REPORT // FBI-WEB")
    out.append(line)
    return "\n".join(out)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/build", methods=["POST"])
def build():
    data = request.get_json(silent=True) or {}
    target = (data.get("target") or "").strip()
    nodes = data.get("nodes") or []
    links = data.get("links") or []

    if not target:
        return jsonify({"ok": False, "error": "Target is required"}), 400

    graph = build_graph(target, nodes, links)
    txt = graph_to_txt(graph)

    safe = "".join(c for c in target if c.isalnum() or c in "-_.")[:40] or "target"
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"fbi_web_{safe}_{stamp}.txt"
    path = os.path.join(REPORTS_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)

    return jsonify({
        "ok": True,
        "graph": graph,
        "txt": txt,
        "filename": filename,
        "download_url": f"/download/{filename}",
    })


@app.route("/download/<path:filename>")
def download(filename):
    path = os.path.join(REPORTS_DIR, filename)
    if not os.path.exists(path):
        return "File not found", 404
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    print("FBI-WEB // OSINT Spider - SalvatoreBonpinsiero")
    print("http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
