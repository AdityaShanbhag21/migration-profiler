# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # --- PAGE CONFIGURATION ---
# st.set_page_config(page_title="Data Migration Profiler", page_icon="📊", layout="wide")

# # --- UPGRADED CUSTOM CSS INJECTION ---
# st.markdown("""
#     <style>
#     #MainMenu {visibility: hidden;}
#     header {visibility: hidden;}
#     footer {visibility: hidden;}
    
#     /* Global background tint */
#     .stApp {
#         background: radial-gradient(circle at top left, #121A2F, #0B0F19);
#     }
    
#     /* Upgraded Metric Cards with Gradients and Hover Glow */
#     div[data-testid="metric-container"] {
#         background: linear-gradient(145deg, #1A1F2B, #222A3A);
#         border: 1px solid #303A52;
#         padding: 20px;
#         border-radius: 12px;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
#         border-top: 4px solid #00E676; /* Vibrant Emerald */
#         transition: all 0.3s ease-in-out;
#     }
    
#     /* Hover effect for interactivity */
#     div[data-testid="metric-container"]:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 20px rgba(0, 230, 118, 0.15);
#         border-top: 4px solid #69F0AE;
#     }
    
#     div[data-testid="stMetricValue"] {
#         font-size: 2.5rem;
#         font-weight: 800;
#         background: -webkit-linear-gradient(#FFFFFF, #B0BEC5);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#     }
    
#     div[data-testid="stMetricLabel"] {
#         color: #90A4AE;
#         font-size: 1.1rem;
#         font-weight: 500;
#         letter-spacing: 0.5px;
#         text-transform: uppercase;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- SIDEBAR: CONSULTING CONTEXT ---
# st.sidebar.title("Migration Engagement")
# st.sidebar.markdown("**Client:** Acme Financial Services")
# st.sidebar.markdown("**Source System:** Legacy SQL Server 2008")
# st.sidebar.markdown("**Target System:** GCP BigQuery")
# st.sidebar.divider()
# st.sidebar.info(
#     "This tool automates pre-migration data discovery by profiling legacy datasets "
#     "for governance, completeness, and structural integrity."
# )

# # --- MAIN APP HEADER ---
# st.title("Automated Data Governance & Migration Readiness Profiler")
# st.markdown("Upload a raw client data extract to instantly assess migration readiness.")

# # --- INGESTION ENGINE ---
# uploaded_file = st.file_uploader("Upload Legacy Dataset (CSV)", type=["csv"])

# if uploaded_file is not None:
#     # Read data
#     df = pd.read_csv(uploaded_file)
    
#     st.divider()
#     st.subheader("1. High-Level Data Topography")
    
#     # --- GOVERNANCE ENGINE (CALCULATIONS) ---
#     total_rows = df.shape[0]
#     total_cols = df.shape[1]
    
#     duplicate_rows = df.duplicated().sum()
#     duplicate_pct = (duplicate_rows / total_rows) * 100
    
#     missing_cells = df.isnull().sum().sum()
#     total_cells = total_rows * total_cols
#     missing_pct = (missing_cells / total_cells) * 100
    
#     # Custom Readiness Scoring Logic
#     # Start at 100, deduct points for duplicates and missing data
#     readiness_score = 100 - (missing_pct * 1.5) - (duplicate_pct * 2)
#     readiness_score = max(0, min(100, readiness_score)) # Keep between 0 and 100
    
#     # Color logic for score
#     if readiness_score > 85:
#         score_color = "normal"
#     elif readiness_score > 60:
#         score_color = "off"
#     else:
#         score_color = "inverse"

#     # --- EXECUTIVE DASHBOARD (KPIs) ---
#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("Total Records", f"{total_rows:,}")
#     col2.metric("Total Attributes (Cols)", total_cols)
#     col3.metric("Overall Missing Data", f"{missing_pct:.1f}%")
#     col4.metric("Migration Readiness Score", f"{readiness_score:.0f}/100", delta_color=score_color)

#     st.divider()
    
#     # --- DETAILED PROFILING VISUALS ---
#     st.subheader("2. Governance & Quality Breakdown")
#     v_col1, v_col2 = st.columns(2)
    
#     with v_col1:
#         st.markdown("**Completeness: Missing Values by Column**")
#         missing_by_col = df.isnull().sum().reset_index()
#         missing_by_col.columns = ['Attribute', 'Missing Count']
#         missing_by_col = missing_by_col[missing_by_col['Missing Count'] > 0]
        
#         if not missing_by_col.empty:
#             fig_missing = px.bar(missing_by_col, x='Attribute', y='Missing Count', 
#                                  color='Missing Count', color_continuous_scale='Reds')
#             # Transparent background for the chart to match the CSS theme
#             fig_missing.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#FFFFFF"))
#             st.plotly_chart(fig_missing, use_container_width=True)
#         else:
#             st.success("No missing values detected across all attributes.")
            
#     with v_col2:
#         st.markdown("**Structural Integrity: Data Type Distribution**")
#         type_counts = df.dtypes.astype(str).value_counts().reset_index()
#         type_counts.columns = ['Data Type', 'Count']
        
#         fig_types = px.pie(type_counts, values='Count', names='Data Type', hole=0.4,
#                            color_discrete_sequence=px.colors.sequential.Teal)
#         # Transparent background for the chart
#         fig_types.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#FFFFFF"))
#         st.plotly_chart(fig_types, use_container_width=True)

#     # --- ACTIONABLE OUTPUT ---
#     st.divider()
#     st.subheader("3. Remediation Actions")
    
#     if duplicate_rows > 0:
#         st.error(f"⚠️ **Critical Risk:** {duplicate_rows} duplicate records found. This will cause primary key collisions in the target database.")
        
#         # Provide download link for dirty rows
#         duplicates_df = df[df.duplicated(keep=False)].sort_values(by=df.columns.tolist())
#         csv_export = duplicates_df.to_csv(index=False).encode('utf-8')
#         st.download_button(
#             label="Download Duplicate Records for Remediation",
#             data=csv_export,
#             file_name='duplicate_records_report.csv',
#             mime='text/csv',
#         )
#     else:
#         st.success("✅ No duplicate records found. Data uniqueness is maintained.")

# else:
#     st.info("Awaiting data extract upload. Please use the file uploader above to begin the profiling sequence.")


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Migration Profiler", page_icon="🛰️", layout="wide")

# ─────────────────────────────────────────────
#  DESIGN SYSTEM — CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

#MainMenu, header, footer { visibility: hidden; }

/* ── Base ── */
.stApp {
    background: #080D1A;
    font-family: 'Inter', sans-serif;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #0D1526 !important;
    border-right: 1px solid #1E2D47;
}
section[data-testid="stSidebar"] * {
    color: #CBD5E1 !important;
}

/* ── Main page padding ── */
.block-container { padding-top: 2rem !important; }

/* ── KPI Cards ── */
div[data-testid="metric-container"] {
    background: #111827;
    border: 1px solid #1E2D47;
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="metric-container"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #22D3EE, #6366F1);
    border-radius: 10px 10px 0 0;
}
div[data-testid="metric-container"]:hover {
    border-color: #22D3EE;
    box-shadow: 0 0 0 1px #22D3EE22, 0 8px 24px rgba(34,211,238,0.08);
}

div[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 2rem !important;
    font-weight: 600 !important;
    color: #F1F5F9 !important;
}
div[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
div[data-testid="stMetricDelta"] svg { display: none; }

/* ── Section headers ── */
.section-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #22D3EE;
    margin-bottom: 0.25rem;
}
.section-title {
    font-size: 1.15rem;
    font-weight: 600;
    color: #E2E8F0;
    margin-bottom: 1.25rem;
}

/* ── Score gauge wrapper ── */
.gauge-card {
    background: #111827;
    border: 1px solid #1E2D47;
    border-radius: 10px;
    padding: 1.5rem;
    text-align: center;
}

/* ── Profile table ── */
.profile-table th {
    color: #64748B !important;
    font-size: 0.7rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    background: #0D1526 !important;
}
.profile-table td {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #CBD5E1 !important;
    background: #111827 !important;
}

/* ── Status pill ── */
.pill {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 99px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.04em;
}
.pill-green  { background:#064E3B; color:#34D399; }
.pill-amber  { background:#451A03; color:#FCD34D; }
.pill-red    { background:#4C0519; color:#FB7185; }
.pill-blue   { background:#0C2044; color:#7DD3FC; }

/* ── Upload area ── */
div[data-testid="stFileUploader"] {
    background: #111827;
    border: 1.5px dashed #1E2D47;
    border-radius: 10px;
    padding: 1rem;
    transition: border-color 0.2s;
}
div[data-testid="stFileUploader"]:hover { border-color: #22D3EE; }

/* ── Divider ── */
hr { border-color: #1E2D47 !important; }

/* ── Expander ── */
div[data-testid="stExpander"] {
    background: #111827 !important;
    border: 1px solid #1E2D47 !important;
    border-radius: 10px !important;
}

/* ── Alert overrides ── */
div[data-testid="stAlert"] {
    border-radius: 8px !important;
}

/* ── Download button ── */
div[data-testid="stDownloadButton"] button {
    background: #0C2044 !important;
    color: #7DD3FC !important;
    border: 1px solid #1D4ED8 !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    transition: all 0.2s;
}
div[data-testid="stDownloadButton"] button:hover {
    background: #1D4ED8 !important;
    color: #fff !important;
}

/* ── Sidebar inputs ── */
div[data-testid="stTextInput"] input {
    background: #0D1526 !important;
    color: #CBD5E1 !important;
    border-color: #1E2D47 !important;
    border-radius: 6px;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  HELPER — PLOTLY CHART THEME
# ─────────────────────────────────────────────
CHART_LAYOUT = dict(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#94A3B8", family="Inter, sans-serif", size=12),
    margin=dict(l=0, r=0, t=10, b=0),
    xaxis=dict(gridcolor="#1E2D47", linecolor="#1E2D47"),
    yaxis=dict(gridcolor="#1E2D47", linecolor="#1E2D47"),
)

ACCENT_PALETTE = ["#22D3EE", "#6366F1", "#F59E0B", "#F43F5E", "#34D399", "#A78BFA"]


# ─────────────────────────────────────────────
#  HELPER — SCORE GAUGE (SVG)
# ─────────────────────────────────────────────
def score_gauge(score: float) -> str:
    """Return an HTML snippet with an SVG arc gauge for the readiness score."""
    pct = score / 100
    radius = 70
    cx, cy = 90, 90
    circumference = 3.14159 * radius  # half-circle
    arc_len = pct * circumference

    if score >= 85:
        color = "#34D399"
        label = "READY"
        label_color = "#34D399"
    elif score >= 60:
        color = "#FCD34D"
        label = "REVIEW"
        label_color = "#FCD34D"
    else:
        color = "#FB7185"
        label = "AT RISK"
        label_color = "#FB7185"

    return f"""
    <div style="text-align:center;">
      <svg width="180" height="110" viewBox="0 0 180 110">
        <!-- Track -->
        <path d="M 20 90 A 70 70 0 0 1 160 90"
              fill="none" stroke="#1E2D47" stroke-width="12" stroke-linecap="round"/>
        <!-- Arc fill -->
        <path d="M 20 90 A 70 70 0 0 1 160 90"
              fill="none" stroke="{color}" stroke-width="12" stroke-linecap="round"
              stroke-dasharray="{arc_len:.1f} {circumference:.1f}"
              style="filter:drop-shadow(0 0 6px {color}88)"/>
        <!-- Score text -->
        <text x="90" y="80" text-anchor="middle"
              font-family="JetBrains Mono, monospace" font-size="28" font-weight="600"
              fill="#F1F5F9">{score:.0f}</text>
        <text x="90" y="100" text-anchor="middle"
              font-family="Inter, sans-serif" font-size="11" font-weight="600"
              letter-spacing="3" fill="{label_color}">{label}</text>
      </svg>
      <p style="color:#64748B;font-size:0.7rem;font-weight:600;letter-spacing:0.1em;
                text-transform:uppercase;margin-top:0.25rem;">Migration Readiness Score</p>
    </div>
    """


# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='display:flex;align-items:center;gap:10px;margin-bottom:1.5rem;'>
      <span style='font-size:1.5rem;'>🛰️</span>
      <div>
        <div style='font-weight:700;font-size:0.95rem;color:#E2E8F0;'>Migration Profiler</div>
        <div style='font-size:0.7rem;color:#475569;letter-spacing:0.06em;'>DATA GOVERNANCE SUITE</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:0.7rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:#475569;margin-bottom:0.5rem;'>Engagement Details</p>", unsafe_allow_html=True)

    client_name    = st.text_input("Client", value="Acme Financial Services")
    source_system  = st.text_input("Source System", value="SQL Server 2008")
    target_system  = st.text_input("Target System", value="GCP BigQuery")

    st.divider()
    st.markdown("""
    <p style='font-size:0.78rem;color:#475569;line-height:1.6;'>
    Profiles legacy datasets for governance, completeness, and structural integrity
    before migration to the target system.
    </p>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<p style='font-size:0.7rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:#475569;margin-bottom:0.75rem;'>Readiness Thresholds</p>", unsafe_allow_html=True)
    st.markdown("""
    <div style='display:flex;flex-direction:column;gap:6px;font-size:0.78rem;'>
      <div style='display:flex;gap:8px;align-items:center;'>
        <span style='width:10px;height:10px;background:#34D399;border-radius:50%;flex-shrink:0;display:inline-block;'></span>
        <span style='color:#94A3B8;'>Ready — Score ≥ 85</span>
      </div>
      <div style='display:flex;gap:8px;align-items:center;'>
        <span style='width:10px;height:10px;background:#FCD34D;border-radius:50%;flex-shrink:0;display:inline-block;'></span>
        <span style='color:#94A3B8;'>Review — Score 60–84</span>
      </div>
      <div style='display:flex;gap:8px;align-items:center;'>
        <span style='width:10px;height:10px;background:#FB7185;border-radius:50%;flex-shrink:0;display:inline-block;'></span>
        <span style='color:#94A3B8;'>At Risk — Score &lt; 60</span>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div style='margin-bottom:1.5rem;'>
  <p style='color:#22D3EE;font-size:0.7rem;font-weight:600;letter-spacing:0.12em;
            text-transform:uppercase;margin:0 0 4px;'>Pre-Migration Assessment</p>
  <h1 style='color:#F1F5F9;font-size:1.6rem;font-weight:700;margin:0 0 6px;'>
    Data Governance Profiler
  </h1>
  <p style='color:#64748B;font-size:0.9rem;margin:0;'>
    Upload a CSV extract to surface data quality risks before migrating to your target system.
  </p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Drop your CSV extract here", type=["csv"], label_visibility="collapsed")
st.markdown("<div style='margin-bottom:0.5rem;'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  MAIN CONTENT — only visible after upload
# ─────────────────────────────────────────────────────────────────────────────
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ── Calculations ──────────────────────────────────────────────────────────
    total_rows  = df.shape[0]
    total_cols  = df.shape[1]

    dup_rows    = int(df.duplicated().sum())
    dup_pct     = (dup_rows / total_rows) * 100

    missing_cells = int(df.isnull().sum().sum())
    total_cells   = total_rows * total_cols
    missing_pct   = (missing_cells / total_cells) * 100

    readiness_score = max(0, min(100, 100 - (missing_pct * 1.5) - (dup_pct * 2)))

    # Per-column profile
    col_profile = pd.DataFrame({
        "Column":       df.columns,
        "Type":         df.dtypes.astype(str).values,
        "Non-Null":     df.notnull().sum().values,
        "Null Count":   df.isnull().sum().values,
        "Null %":       (df.isnull().mean() * 100).round(1).values,
        "Unique":       df.nunique().values,
        "Uniqueness %": (df.nunique() / total_rows * 100).round(1).values,
    })

    # ── SECTION 1 — KPI Row ───────────────────────────────────────────────────
    st.divider()
    st.markdown('<p class="section-label">Overview</p><p class="section-title">Data Topography</p>', unsafe_allow_html=True)

    kpi1, kpi2, kpi3, kpi4, gauge_col = st.columns([1.2, 1.2, 1.2, 1.2, 1.6])

    kpi1.metric("Total Records",     f"{total_rows:,}")
    kpi2.metric("Columns",           total_cols)
    kpi3.metric("Missing Data",      f"{missing_pct:.1f}%",
                delta=f"{missing_cells:,} cells", delta_color="inverse" if missing_pct > 5 else "off")
    kpi4.metric("Duplicate Rows",    f"{dup_rows:,}",
                delta=f"{dup_pct:.1f}% of total", delta_color="inverse" if dup_pct > 0 else "off")

    with gauge_col:
        st.markdown(score_gauge(readiness_score), unsafe_allow_html=True)

    # ── SECTION 2 — Charts ────────────────────────────────────────────────────
    st.divider()
    st.markdown('<p class="section-label">Quality Analysis</p><p class="section-title">Governance Breakdown</p>', unsafe_allow_html=True)

    chart_l, chart_r = st.columns(2)

    # Missing values bar chart
    with chart_l:
        st.markdown("<p style='color:#94A3B8;font-size:0.8rem;font-weight:600;margin-bottom:0.5rem;'>Null Values by Column (%)</p>", unsafe_allow_html=True)
        missing_by_col = col_profile[col_profile["Null Count"] > 0].sort_values("Null %", ascending=True)

        if not missing_by_col.empty:
            fig_missing = px.bar(
                missing_by_col,
                x="Null %", y="Column",
                orientation="h",
                color="Null %",
                color_continuous_scale=[[0, "#22D3EE"], [0.4, "#F59E0B"], [1, "#F43F5E"]],
                text="Null %",
            )
            fig_missing.update_traces(texttemplate="%{text:.1f}%", textposition="outside",
                                      marker_line_width=0)
            fig_missing.update_coloraxes(showscale=False)
            fig_missing.update_layout(**CHART_LAYOUT)
            st.plotly_chart(fig_missing, use_container_width=True)
        else:
            st.markdown("""
            <div style='background:#064E3B22;border:1px solid #064E3B;border-radius:8px;
                        padding:1.5rem;text-align:center;margin-top:0.5rem;'>
              <p style='color:#34D399;font-size:0.9rem;font-weight:600;margin:0;'>
                ✓ Zero null values detected
              </p>
            </div>
            """, unsafe_allow_html=True)

    # Data type donut
    with chart_r:
        st.markdown("<p style='color:#94A3B8;font-size:0.8rem;font-weight:600;margin-bottom:0.5rem;'>Schema — Data Type Distribution</p>", unsafe_allow_html=True)
        type_counts = df.dtypes.astype(str).value_counts().reset_index()
        type_counts.columns = ["Data Type", "Count"]

        fig_types = px.pie(
            type_counts, values="Count", names="Data Type",
            hole=0.55,
            color_discrete_sequence=ACCENT_PALETTE,
        )
        fig_types.update_traces(textinfo="label+percent", textfont_size=11)
        fig_types.update_layout(**CHART_LAYOUT, showlegend=False)
        st.plotly_chart(fig_types, use_container_width=True)

    # ── SECTION 3 — Column Profile Table ─────────────────────────────────────
    st.divider()
    st.markdown('<p class="section-label">Deep Dive</p><p class="section-title">Column-Level Profile</p>', unsafe_allow_html=True)

    def null_pill(pct):
        if pct == 0:   return f'<span class="pill pill-green">0%</span>'
        elif pct < 10: return f'<span class="pill pill-amber">{pct}%</span>'
        else:          return f'<span class="pill pill-red">{pct}%</span>'

    def type_pill(t):
        color = "pill-blue" if "int" in t or "float" in t else "pill-green" if "object" in t else "pill-amber"
        return f'<span class="pill {color}">{t}</span>'

    display_profile = col_profile.copy()
    display_profile["Null %"]  = display_profile["Null %"].apply(null_pill)
    display_profile["Type"]    = display_profile["Type"].apply(type_pill)

    table_html = display_profile[["Column", "Type", "Non-Null", "Null Count", "Null %", "Unique", "Uniqueness %"]].to_html(
        index=False, escape=False,
        classes="profile-table",
    )
    st.markdown(f"""
    <style>
    .profile-table {{ width:100%; border-collapse:collapse; }}
    .profile-table th, .profile-table td {{
        padding: 0.55rem 0.9rem; text-align:left;
        border-bottom: 1px solid #1E2D47;
    }}
    .profile-table tr:last-child td {{ border-bottom: none; }}
    .profile-table tr:hover td {{ background: #0D1526 !important; }}
    </style>
    <div style='background:#111827;border:1px solid #1E2D47;border-radius:10px;overflow:hidden;'>
      {table_html}
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 4 — Null Heatmap ──────────────────────────────────────────────
    if missing_pct > 0:
        st.divider()
        st.markdown('<p class="section-label">Visualisation</p><p class="section-title">Null Distribution Heatmap</p>', unsafe_allow_html=True)
        st.markdown("<p style='color:#64748B;font-size:0.8rem;margin-bottom:0.75rem;'>Each cell represents a row-column pair. Dark = present, bright = null. Useful for spotting systematic gaps.</p>", unsafe_allow_html=True)

        # Sample if large
        sample_df = df.head(200) if total_rows > 200 else df
        null_matrix = sample_df.isnull().astype(int)

        fig_heat = px.imshow(
            null_matrix.T,
            color_continuous_scale=[[0, "#111827"], [1, "#F43F5E"]],
            aspect="auto",
        )
        fig_heat.update_coloraxes(showscale=False)
        fig_heat.update_layout(**CHART_LAYOUT, height=max(150, total_cols * 28))
        fig_heat.update_xaxes(title="Row index", showgrid=False)
        fig_heat.update_yaxes(title="", tickfont=dict(size=11))
        st.plotly_chart(fig_heat, use_container_width=True)

    # ── SECTION 5 — Remediation Actions ──────────────────────────────────────
    st.divider()
    st.markdown('<p class="section-label">Action Required</p><p class="section-title">Remediation Checklist</p>', unsafe_allow_html=True)

    action_col1, action_col2 = st.columns(2)

    with action_col1:
        # Duplicates
        if dup_rows > 0:
            st.error(f"**{dup_rows} duplicate rows** detected — this will cause primary key collisions in {target_system}.")
            with st.expander(f"Preview duplicate records ({min(dup_rows, 10)} shown)"):
                dup_preview = df[df.duplicated(keep=False)].sort_values(by=df.columns.tolist()).head(10)
                st.dataframe(dup_preview, use_container_width=True, hide_index=True)

            dup_csv = df[df.duplicated(keep=False)].sort_values(by=df.columns.tolist()).to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇ Export Duplicate Records",
                data=dup_csv,
                file_name="duplicate_records.csv",
                mime="text/csv",
            )
        else:
            st.success("**No duplicates found.** Data uniqueness is confirmed.")

    with action_col2:
        # Missing data columns
        high_null_cols = col_profile[col_profile["Null %"] > 20]
        if not high_null_cols.empty:
            st.warning(f"**{len(high_null_cols)} column(s)** exceed 20% null threshold — review before migration.")
            for _, row in high_null_cols.iterrows():
                st.markdown(f"<span class='pill pill-amber'>{row['Column']}</span>&nbsp; <span style='color:#64748B;font-size:0.8rem;'>{row['Null %']}% null</span>", unsafe_allow_html=True)
        else:
            st.success("**All columns within null thresholds** (< 20%).")

    # ── Full dataset preview ──────────────────────────────────────────────────
    st.divider()
    with st.expander("Raw Data Preview (first 100 rows)"):
        st.dataframe(df.head(100), use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────
#  EMPTY STATE
# ─────────────────────────────────────────────
else:
    st.markdown("""
    <div style='background:#111827;border:1px dashed #1E2D47;border-radius:12px;
                padding:3rem 2rem;text-align:center;margin-top:1rem;'>
      <div style='font-size:2.5rem;margin-bottom:1rem;'>📂</div>
      <p style='color:#E2E8F0;font-weight:600;font-size:1rem;margin:0 0 8px;'>
        No dataset loaded
      </p>
      <p style='color:#475569;font-size:0.85rem;margin:0;'>
        Drop a CSV extract above to begin the profiling sequence.
      </p>
    </div>
    """, unsafe_allow_html=True)
    