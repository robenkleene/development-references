# React

## Stateless Functions

Components declared with `const` are "stateless components" (i.e., there's no properties on `this`).

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

Which is equivalent to:

``` javascript
const IndexPage = ({ data }) => {
  return (
    <Layout>
      <SEO title="Home" />
      <div
        dangerouslySetInnerHTML={{
          __html: data.allMarkdownRemark.nodes[0].html,
        }}
      />
    </Layout>
  )
}
```