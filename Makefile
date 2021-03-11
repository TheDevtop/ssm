help:
	@echo "make help/build/clean"
build:
	@mkdir bin
	@go fmt
	@go build -o bin/ssm-go
	@cp state.py bin/ssm-py
	@chmod a+x bin/ssm-py
clean:
	@rm -rf bin
