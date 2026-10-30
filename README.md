# Universal Human + AI Security Shield & Guardrail Platform

A Zero-Access, Network-Level security platform designed to protect enterprises from both malicious AI interactions (e.g., Jailbreaks, DarkGPT, Rogue Agents) and Insider Human Threats (e.g., Data Leaks, Unauthorized USB writes, Malware deployment).

## Core Architecture
- **Zero-Access Enforcement:** Operates entirely via Network Gateway Interception (Mitmproxy) and lightweight app-level scripts. No OS Root/Admin rights required.
- **5-Pass Security Audit Loop:** Every single outbound prompt or inbound message passes through a real-time, multi-stage validation engine before execution.
- **Insider Threat Management:** Dynamic network/peripheral filter blocking unauthorized internal exfiltration attempts.

## Project Structure
- `network_interceptor.py`: Catches and pauses AI API traffic in real-time.
- `security_audit_loop.py`: Executes the 5-pass vulnerability check.
- `hardware_monitor.py`: Defends endpoints from physical USB and script insertion.
