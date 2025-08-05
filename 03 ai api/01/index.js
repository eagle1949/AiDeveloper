import fetch from 'node-fetch';
globalThis.fetch = fetch;

import { OpenAI } from 'openai';


// 连接到本地LM Studio服务器
const localAI = new OpenAI({
  baseURL: 'http://localhost:1234/v1', // LM Studio默认端口
  apiKey: 'lm-studio', // 本地不需要真实key，但需要提供
});

// 调用本地Qwen7B
async function generateTextLocal(prompt) {
  try {
    const completion = await localAI.chat.completions.create({
      messages: [{ role: "user", content: prompt }],
      model: "qwen", // 使用你加载的模型名称
      temperature: 0.7,
      max_tokens: 500,
    });
    return completion.choices[0].message.content;
  } catch (error) {
    console.error('本地模型调用失败:', error);
    throw error;
  }
}

// 测试连接
async function testLocalModel() {
  const response = await generateTextLocal("你好，请介绍一下你自己");
  console.log('Qwen7B响应:', response);
}


testLocalModel().catch(console.error);