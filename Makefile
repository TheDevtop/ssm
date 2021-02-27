help:
	@echo "make help/build/clean"
build:
	@mkdir bin
	@cp state.py bin/ssm
	@chmod a+x bin/ssm
	@echo "Done!"
clean:
	@rm -rf bin
	@echo "Done!"
