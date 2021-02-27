import React from "react"
import Layout from "../components/layout"

const StaticKedroViz = React.lazy(() =>
    import("../components/StaticKedroViz")
)

const IndexPage = () => {
    const isSSR = typeof window === "undefined"

    return (
      <Layout>
        {!isSSR && (
          <React.Suspense fallback={<div />}>
            <StaticKedroViz />
          </React.Suspense>
        )}
      </Layout>
    )
  }

export default IndexPage
