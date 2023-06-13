# Introduction

This project provides connector for Kafka Connect to read data from Github.

# Documentation

Documentation on the connector is hosted on Confluent's
[docs site](https://docs.confluent.io/current/connect/kafka-connect-github/).

Source code is located in Confluent's
[docs repo](https://github.com/confluentinc/docs/tree/master/connect/kafka-connect-github). If changes
are made to configuration options for the connector, be sure to generate the RST docs (as described
below) and open a PR against the docs repo to publish those changes!

# Configs

Documentation on the configurations for each connector can be automatically generated via Maven.

To generate documentation for the source connector:
```bash
mvn -Pdocs exec:java@source-config-docs
```

# Compatibility:

This connector has been tested against the Confluent Platform and supports compatibility with versions 5.0.x and above.

# Integration Tests

To run ITs in your local environment, please export the GITHUB_CREDS environment variable to
 the path of your credentials file, which must be in a JSON format.
```bash
export GITHUB_CREDS=path/to/your/creds.json
```

An example credentials file:
```$xslt
{
  "creds": {
    "github_oauth": <your_github_oauth_token>,
  }
}
```

You can run `vault kv get v1/ci/kv/connect/github_it` to obtain Github credentials that 
can be used to populate a credentials file.