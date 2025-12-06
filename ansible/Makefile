ansible-playbook:
	ANSIBLE_HOST_KEY_CHECKING=False \
	ansible-playbook -i $(ANSIBLE_INVENTORY) $(ANSIBLE_PLAYBOOK) --extra-vars "client_port=$(client_port) anthropic_api_key=$(anthropic_api_key) app_user=$(app_user) gallery_url=$(gallery_url)" 