import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"
import KedroViz from '@quantumblack/kedro-viz';

class IndexPage extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      pipelineData: undefined
    }
    this.componentDidMount = () => {
      fetch('/pipeline.json')
        .then(response => response.json())
        .then(data => this.setState({ pipelineData: data }))
    }
  }
  render() {
    return (
      <Layout>
        {/* <SEO title="Home" /> */}
        <div className="pipeline" style={{ minHeight: '80vh' }}>
          {this.state.pipelineData === undefined ? 'loading' : <KedroViz style={{ height: '80vh' }} data={this.state.pipelineData} />}
        </div>
      </Layout>
    )
  }
}

export default IndexPage
