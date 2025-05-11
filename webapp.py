import streamlit as st
import ast
from analyzer.python_analyzer import ComplexityAnalyzer
from utils.loc_counter import count_loc_comments
from utils.gpt_helper import get_refactor_suggestion
from analyzer.cfg_drawer import draw_cfg
import matplotlib.pyplot as plt

# Cấu hình giao diện Streamlit
st.set_page_config(page_title="Cyclomatic Analyzer", layout="wide")
st.title("🧠 Phân tích độ phức tạp mã nguồn (McCabe’s Cyclomatic Complexity)")

# Chọn loại input: thủ công hoặc tải file
input_type = st.radio("Chọn cách nhập code:", ["Nhập thủ công", "Tải file"])
code_input = ""

if input_type == "Nhập thủ công":
    code_input = st.text_area("Nhập mã Python:", height=300)
else:
    uploaded_file = st.file_uploader("Tải lên file .py", type=["py"])
    if uploaded_file:
        code_input = uploaded_file.read().decode("utf-8")
        st.code(code_input, language='python')

if st.button("🔍 Phân tích"):
    if not code_input.strip():
        st.warning("Vui lòng nhập mã nguồn hoặc tải file.")
    else:
        results = []
        try:
            tree = ast.parse(code_input)
            for node in tree.body:
                if isinstance(node, ast.FunctionDef):
                    analyzer = ComplexityAnalyzer()
                    analyzer.visit(node)
                    score = analyzer.complexity
                    suggestion = get_refactor_suggestion(node, code_input)
                    results.append({
                        "name": node.name,
                        "score": score,
                        "suggestion": suggestion,
                        "cfg": analyzer.cfg_edges
                    })

            loc, comments = count_loc_comments(code_input)
            st.markdown(f"**📄 Tổng dòng mã:** `{loc}` – 📝 **Dòng comment:** `{comments}`")

            for r in results:
                st.subheader(f"🔹 `{r['name']}` – Complexity: `{r['score']}`")
                st.markdown(f"> 💡 **Gợi ý refactor:**\n{r['suggestion']}")
                st.markdown("**Biểu đồ CFG:**")
                draw_cfg(r['cfg'])

            if results:
                fig, ax = plt.subplots()
                ax.bar([r["name"] for r in results], [r["score"] for r in results], color='lightblue')
                ax.axhline(10, color='red', linestyle='--', label='Ngưỡng phức tạp')
                ax.set_xlabel("Tên hàm")
                ax.set_ylabel("Độ phức tạp McCabe")
                ax.set_title("Biểu đồ độ phức tạp McCabe theo hàm")
                ax.legend()
                st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Lỗi khi phân tích: {e}")
