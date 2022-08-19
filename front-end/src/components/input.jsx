import { Input, Button } from 'antd';
import React, { useState } from 'react';


function submitPrompt (e){
    console.log(e.target.value)
}

function UserInput() {
    const [userInput, setUserInput] = useState("");

    return <div>
        <Input.Group compact>
          <Input
          onChange = {(e)=>setUserInput(e)}
        defaultValue="Enter Prompt"
      />
      <Button type="primary" onClick={() => submitPrompt(userInput)}>Submit</Button>
        </Input.Group>
        </div>;
  }


export default UserInput;