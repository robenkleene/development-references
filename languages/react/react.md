# React

## Stateless Functions

Components declared with `const` are "stateless components" (i.e., there's no properties on `this`).

``` javascript
const IndexPage = ({ data }) => (
  <Layout>
    <SEO title="Home" />
    <h1>Hi people</h1>
    <p>Welcome to your new Gatsby site.</p>
    <p>Now go build something great.</p>
    <div dangerouslySetInnerHTML={{ __html: data.allMarkdownRemark.nodes[0].html }} />
    <div>
      <ExampleImage />
    </div>
    <ExampleList />
    <ExampleButton />
  </Layout>
)
```