# To generate

1. Bump the version in `config.json`
2. Download Swagger codegen

    ```bash
    wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.18/swagger-codegen-cli-2.4.18.jar -O swagger-codegen-cli.jar
    ```

3. Generate the Gate swagger
    a. Clone the gate repo: <https://github.com/spinnaker/gate>
    b. In it, run `sh swagger/generate_swagger.sh`
4. Run Swagger codegen

    ```bash
    java -jar ./swagger-codegen-cli.jar generate -i <PATH_TO_GATE>/swagger/swagger.json -l python -c ./config.json
    ```
