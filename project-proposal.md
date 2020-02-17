# Cloudmesh Cloud AI Service

As part of the Cloud Service AI project there is opportunity to expand the current available AI services exposed as endpoints in Cloudmesh. The current offerings include Azure and Chameleon cloud. I would like to propose expanding the available AI Service API endpoints to in include clustering functionality from available python packages like scikit-learn. Specifically, I would like to expose K-means analysis as an endpoint for the users of Cloudmesh for Azure. Secondly, the current architecture of Cloudmesh appears to only create the endpoints on localhost and benchmark against the users machine, I would like to open a new route to Google Cloud services and Azure. If possible, with available time, perform a benchmark analysis of the AI service running in Google Cloud. 

## Outline of proposed work

1. Create a K-means Class in cloudmesh-analytics that can read User's parameters
2. Create the OpenAPI spec for K-Means endpoint and determine which endpoints to create
3. Create logic to spin up the services on a server on Google Cloud and Azure 

## Secondary options for proposed work

1. Create a command line interface for K-means
2. Create a command line interface for allocating K-means services to Azure and/or Google servers