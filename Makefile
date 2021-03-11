help:
	@echo "make help/build/clean"
build:
	@mkdir bin
	@go fmt
	@go build -o bin/gossm
	@cp state.py bin/ssm
	@chmod a+x bin/ssm
clean:
	@rm -rf bin
