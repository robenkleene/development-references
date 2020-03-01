# Postman

## GraphQL

To send a GraphQL request:

1. In the "Headers" tab, add `Content-Type: application/graphql`
2. In the "Body" tab, select "Raw" and enter the query, e.g.:

	query GetLaunches {
		launches {
			id
			mission {
			  name
			}
		}
	}
