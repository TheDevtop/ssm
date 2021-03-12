help:
	@echo "SSM Makefile"
	@echo "make help/build/clean"
build:
	@mkdir bin
	@go fmt ssm.go
	@go build -o bin/ssm-go ssm.go
	@cp ssm.py bin/ssm-py
	@chmod a+x bin/ssm-py
clean:
	@rm -rf bin
