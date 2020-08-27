# React

## Stateless Components

Components declared with `const` are "stateless" (i.e., there's no properties on `this`).

``` javascript
const IndexPage = ({ data }) => (
  <Layout>
    <SEO title="Home" />
    <div
      dangerouslySetInnerHTML={{ __html: data.allMarkdownRemark.nodes[0].html }}
    />
  </Layout>
)
```

This can also be written like this, which allows 

``` javascript
const IndexPage = ({ data }) => {
  const { allMarkdownRemark } = data
  return (
    <Layout>
      <SEO title="Home" />
      <div
        dangerouslySetInnerHTML={{
          __html: allMarkdownRemark.nodes[0].html,
        }}
      />
    </Layout>
  )
}
```