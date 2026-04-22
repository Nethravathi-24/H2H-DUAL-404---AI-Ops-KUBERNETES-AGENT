import sys
import os
import time
import subprocess
import streamlit as st

# Fix import path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# Project imports
from agent.reasoning.root_cause_engine import get_root_cause
from agent.reasoning.recommendation_engine import generate_recommendations
from agent.reasoning.health_summary import get_cluster_summary
from agent.reasoning.explanation_engine import generate_explanations
from agent.reasoning.history_engine import (
    log_issues,
    get_recent_history
)
from agent.reasoning.risk_engine import calculate_risk
from agent.nl_query_engine import process_query


# -------------------------------
# Helper: Get Pod List
# -------------------------------

def get_pod_list():

    try:

        result = subprocess.run(
            ["kubectl", "get", "pods", "-o", "name"],
            capture_output=True,
            text=True
        )

        pods = result.stdout.splitlines()

        pod_names = [
            p.replace("pod/", "")
            for p in pods
        ]

        return pod_names

    except Exception:

        return []


# -------------------------------
# Helper: Fetch Logs
# -------------------------------

def get_pod_logs(pod_name):

    try:

        result = subprocess.run(
            ["kubectl", "logs", pod_name],
            capture_output=True,
            text=True
        )

        logs = result.stdout

        if logs:

            return logs[:800]

        return "No logs available."

    except Exception:

        return "Unable to fetch logs."


# -------------------------------
# Main Dashboard
# -------------------------------

def run_dashboard():

    st.set_page_config(
        page_title="AI Ops Kubernetes Assistant",
        page_icon="🤖",
        layout="wide"
    )

    st.title("🤖 AI Ops Kubernetes Dashboard")

    st.markdown("---")

    # Sidebar Controls

    st.sidebar.header("⚙️ Controls")

    refresh_rate = st.sidebar.slider(
        "Auto Refresh (seconds)",
        5,
        60,
        10
    )

    show_logs = st.sidebar.checkbox(
        "Show Pod Logs",
        value=True
    )

    st.sidebar.markdown("---")

    # ---------------------------
    # Natural Language AI Query
    # ---------------------------

    st.subheader("🧠 Ask AI About Cluster")

    user_query = st.text_input(
        "Try: pod status | failing pods | memory usage"
    )

    if user_query:

        response = process_query(
            user_query
        )

        st.text_area(
            "🤖 AI Response",
            response,
            height=300
        )

    st.markdown("---")

    # ---------------------------
    # Cluster Summary
    # ---------------------------

    summary = get_cluster_summary()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Pods",
        summary["total"]
    )

    col2.metric(
        "Running Pods",
        summary["running"]
    )

    col3.metric(
        "Failing Pods",
        summary["failing"]
    )

    # ---------------------------
    # Risk Level
    # ---------------------------

    risk_level, risk_icon = calculate_risk(summary)

    st.subheader("🚨 Cluster Risk Level")

    if risk_level == "HIGH":

        st.error(
            f"{risk_icon} Cluster Risk: {risk_level}"
        )

    elif risk_level == "MEDIUM":

        st.warning(
            f"{risk_icon} Cluster Risk: {risk_level}"
        )

    else:

        st.success(
            f"{risk_icon} Cluster Risk: {risk_level}"
        )

    st.markdown("---")

    # ---------------------------
    # Issues Section
    # ---------------------------

    st.subheader("⚠️ Issues Detected")

    issues = get_root_cause()

    if issues:

        log_issues(issues)

        for issue in issues:

            st.warning(issue)

    else:

        st.success(
            "✅ No issues detected."
        )

    st.markdown("---")

    # ---------------------------
    # Root Cause Explanation
    # ---------------------------

    st.subheader("🧠 Root Cause Analysis")

    explanations = generate_explanations(
        issues
    )

    if explanations:

        for exp in explanations:

            st.info(exp)

    else:

        st.success(
            "No root causes detected."
        )

    st.markdown("---")

    # ---------------------------
    # Recommendations
    # ---------------------------

    st.subheader("📌 Suggested Fixes")

    recommendations = generate_recommendations(
        issues
    )

    if recommendations:

        for rec in recommendations:

            st.info(rec)

    else:

        st.success(
            "Cluster is healthy."
        )

    st.markdown("---")

    # ---------------------------
    # Pod Logs Viewer
    # ---------------------------

    if show_logs:

        st.subheader("📄 Pod Logs Viewer")

        pod_list = get_pod_list()

        if pod_list:

            selected_pod = st.selectbox(
                "Select Pod",
                pod_list
            )

            if selected_pod:

                logs = get_pod_logs(
                    selected_pod
                )

                st.text_area(
                    "Logs",
                    logs,
                    height=300
                )

        else:

            st.warning(
                "No pods found."
            )

    st.markdown("---")

    # ---------------------------
    # Failure History
    # ---------------------------

    st.subheader("📈 Failure History")

    history = get_recent_history()

    if history:

        for entry in history:

            st.text(
                f"{entry['time']} — {entry['issue']}"
            )

    else:

        st.success(
            "No historical failures recorded."
        )

    # ---------------------------
    # Auto Refresh
    # ---------------------------

    time.sleep(refresh_rate)

    st.rerun()


# -------------------------------

if __name__ == "__main__":

    run_dashboard()
