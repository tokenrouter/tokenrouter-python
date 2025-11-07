# Responses

Types:

```python
from tokenrouter.types import ResponseObject
```

Methods:

- <code title="post /v1/responses">client.responses.<a href="./src/tokenrouter/resources/responses.py">create</a>(\*\*<a href="src/tokenrouter/types/response_create_params.py">params</a>) -> <a href="./src/tokenrouter/types/response_object.py">ResponseObject</a></code>
- <code title="post /v1/responses/{request_id}">client.responses.<a href="./src/tokenrouter/resources/responses.py">replay</a>(request_id, \*\*<a href="src/tokenrouter/types/response_replay_params.py">params</a>) -> <a href="./src/tokenrouter/types/response_object.py">ResponseObject</a></code>

# RoutingRules

Types:

```python
from tokenrouter.types import (
    RoutingRule,
    RoutingRuleCreateResponse,
    RoutingRuleRetrieveResponse,
    RoutingRuleUpdateResponse,
    RoutingRuleListResponse,
    RoutingRuleDeleteResponse,
)
```

Methods:

- <code title="post /v1/routing-rules">client.routing_rules.<a href="./src/tokenrouter/resources/routing_rules.py">create</a>(\*\*<a href="src/tokenrouter/types/routing_rule_create_params.py">params</a>) -> <a href="./src/tokenrouter/types/routing_rule_create_response.py">RoutingRuleCreateResponse</a></code>
- <code title="get /v1/routing-rules/{id}">client.routing_rules.<a href="./src/tokenrouter/resources/routing_rules.py">retrieve</a>(id) -> <a href="./src/tokenrouter/types/routing_rule_retrieve_response.py">RoutingRuleRetrieveResponse</a></code>
- <code title="patch /v1/routing-rules/{id}">client.routing_rules.<a href="./src/tokenrouter/resources/routing_rules.py">update</a>(id, \*\*<a href="src/tokenrouter/types/routing_rule_update_params.py">params</a>) -> <a href="./src/tokenrouter/types/routing_rule_update_response.py">RoutingRuleUpdateResponse</a></code>
- <code title="get /v1/routing-rules">client.routing_rules.<a href="./src/tokenrouter/resources/routing_rules.py">list</a>() -> <a href="./src/tokenrouter/types/routing_rule_list_response.py">RoutingRuleListResponse</a></code>
- <code title="delete /v1/routing-rules/{id}">client.routing_rules.<a href="./src/tokenrouter/resources/routing_rules.py">delete</a>(id) -> <a href="./src/tokenrouter/types/routing_rule_delete_response.py">RoutingRuleDeleteResponse</a></code>

# FirewallRules

Types:

```python
from tokenrouter.types import (
    FirewallRule,
    FirewallRuleCreateResponse,
    FirewallRuleRetrieveResponse,
    FirewallRuleUpdateResponse,
    FirewallRuleListResponse,
    FirewallRuleDeleteResponse,
)
```

Methods:

- <code title="post /v1/firewall-rules">client.firewall_rules.<a href="./src/tokenrouter/resources/firewall_rules.py">create</a>(\*\*<a href="src/tokenrouter/types/firewall_rule_create_params.py">params</a>) -> <a href="./src/tokenrouter/types/firewall_rule_create_response.py">FirewallRuleCreateResponse</a></code>
- <code title="get /v1/firewall-rules/{id}">client.firewall_rules.<a href="./src/tokenrouter/resources/firewall_rules.py">retrieve</a>(id) -> <a href="./src/tokenrouter/types/firewall_rule_retrieve_response.py">FirewallRuleRetrieveResponse</a></code>
- <code title="patch /v1/firewall-rules/{id}">client.firewall_rules.<a href="./src/tokenrouter/resources/firewall_rules.py">update</a>(id, \*\*<a href="src/tokenrouter/types/firewall_rule_update_params.py">params</a>) -> <a href="./src/tokenrouter/types/firewall_rule_update_response.py">FirewallRuleUpdateResponse</a></code>
- <code title="get /v1/firewall-rules">client.firewall_rules.<a href="./src/tokenrouter/resources/firewall_rules.py">list</a>() -> <a href="./src/tokenrouter/types/firewall_rule_list_response.py">FirewallRuleListResponse</a></code>
- <code title="delete /v1/firewall-rules/{id}">client.firewall_rules.<a href="./src/tokenrouter/resources/firewall_rules.py">delete</a>(id) -> <a href="./src/tokenrouter/types/firewall_rule_delete_response.py">FirewallRuleDeleteResponse</a></code>
