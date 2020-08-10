# GatsbyJS GraphQL

## GraphiQL

GraphiQL is a GraphQL IDE. To access it in your Gatsby project:

1. Start the development server if it's not already running (`gatsby develop`).
2. Visit `http://localhost:8000/___graphql` in a browser

### Data

You can explore the data in GraphQL by using the sidebar. For example, if you've added Markdown with `gatsby-transformer-remark` then that data will appear under `markdownRemark`. E.g., to see the compiled HTML by clicking the "`markdownRemark` > `html`" checkbox (ignore the `html:` with a disclosure triangle), and then running the resulting query:

    query MyQuery {
        markdownRemark {
            html
        }
    }

### Page Queries

An example of querying for the site metadata description:

    export const query = graphql`
    query HomePageQuery {
        site {
        siteMetadata {
            description
        }
        }
    }
    `

An example of accessing that data in a component:

    const HomePage = () => {
    const HomePage = ({data}) => {
        return (
            <div>
            Hello!
            {data.site.siteMetadata.description}
            </div>
        )
    }

`set.siteMetadata.description` is exactly where the data is in the hierarchy in the GraphiQL browser.