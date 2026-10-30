"""
Aegis Core: Network Interceptor via Mitmproxy API
Intercepts and inspects all outbound text/SMS requests going to AI APIs.
"""
import json
from security_audit_loop import SecurityAuditLoop

class AIRequestInterceptor:
    def __init__(self):
        # Hamare 5-Pass Core Loop Brain ko initialize karna
        self.security_shield = SecurityAuditLoop()

    def request(self, flow):
        # Agar traffic kisi AI API (like OpenAI, Claude, or custom DarkGPT endpoints) ki taraf ja rahi hai
        if "://openai.com" in flow.request.pretty_host or "://anthropic.com" in flow.request.pretty_host:
            try:
                request_data = json.loads(flow.request.content.decode("utf-8"))
                # Prompt/Message ko extract karna
                user_prompt = ""
                if "messages" in request_data:
                    user_prompt = request_data["messages"][-1]["content"]
                
                if user_prompt:
                    print(f"[!] Intercepted Outbound Prompt: {user_prompt}")
                    
                    # Message ko Hamare 5-Pass Check System mein bhejna
                    is_safe, failure_reason = self.security_shield.run_5_pass_audit(user_prompt)
                    
                    if not is_safe:
                        print(f"[RED ALERT] Threat Blocked! Reason: {failure_reason}")
                        # Traffic ko AI tak jaane se pehle hi raste mein BLOCK karna aur error return karna
                        flow.response = mitmproxy.http.Response.make(
                            403, 
                            f"Access Denied by Security Shield. Violation: {failure_reason}".encode("utf-8"),
                            {"Content-Type": "text/plain"}
                        )
            except Exception as e:
                print(f"Error parsing request payload: {str(e)}")

addons = [AIRequestInterceptor()]
