REGISTRY="ghcr.io"
ORG="dcostersabin"

.ONSHELL:
build-subdomain:
	@docker build -t $(REGISTRY)/$(ORG)/thm_subdomain:latest -f subdomain/Dockerfile subdomain/;
	@docker push $(REGISTRY)/$(ORG)/thm_subdomain:latest

.ONSHELL:
build-port-scanner:
	@docker build -t $(REGISTRY)/$(ORG)/thm_port_scanner:latest -f port-scan/Dockerfile port-scan/;
	@docker push $(REGISTRY)/$(ORG)/thm_port_scanner:latest


.ONSHELL:
build-controller:
	@docker build -t $(REGISTRY)/$(ORG)/thm_controller:latest -f controller/docker/Dockerfile controller/;
	@docker push $(REGISTRY)/$(ORG)/thm_controller:latest

.ONSHELL:
build-collector:
	@docker build -t $(REGISTRY)/$(ORG)/thm_the_collector:latest -f the-collector/docker/Dockerfile the-collector/;
	@docker push $(REGISTRY)/$(ORG)/thm_the_collector:latest
