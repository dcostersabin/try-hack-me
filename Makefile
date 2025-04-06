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
