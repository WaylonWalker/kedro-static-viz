import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"
import data from './pipeline.json'
import KedroViz from '@quantumblack/kedro-viz';

class IndexPage extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      loaded: false
    }
    this.componentDidMount = () => {
      this.setState({ loaded: true })
    }
  }
  render() {
    return (
      <Layout>
        <SEO title="Home" />
        <div className="pipeline" style={{ minHeight: '80vh' }}>
          {this.state.loaded === false ? 'loading' : <KedroViz style={{ height: '80vh' }} data={data} />}
        </div>
      </Layout>
    )
  }
}

export default IndexPage
