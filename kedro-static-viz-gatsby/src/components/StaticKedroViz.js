import React from "react"
import KedroViz from '@quantumblack/kedro-viz';

class StaticKedroViz extends React.Component {
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
        <div className="pipeline" style={{ minHeight: '80vh' }}>
          {this.state.pipelineData === undefined ? 'loading' : <KedroViz style={{ height: '80vh' }} data={this.state.pipelineData} />}
        </div>
    )
  }
}

export default StaticKedroViz
