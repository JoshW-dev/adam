import React, { useState } from 'react'
import { Button, Input} from 'antd';

function UserInput() {
    const [input, setInput] = useState("")

    var updateInputState = (e) => {
        const { value } = e.target
        setInput(prevState => ({
            ...prevState,
            value
        }))
    }
    return (
        <div>
            <Input bordered={false} placeholder="Dreams" onChange={updateInputState} />
        </div>
    )
}
export default UserInput