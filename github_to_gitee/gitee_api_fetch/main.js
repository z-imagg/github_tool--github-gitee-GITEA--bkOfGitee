/*
npm init
npm install   chrome-remote-interface
*/
const CDP = require('chrome-remote-interface');

async function intercept(url) {
  let client;
  try {
    client = await CDP();
    const { Network, Page, Fetch } = client;
    
    // 所有网络请求发出前触发，打印能看到请求的url
    Network.requestWillBeSent((params) => {
      console.log(params.request.url);
    });
    
    Fetch.requestPaused((params) => {
      // 拦截到请求并返回自定义body
      Fetch.fulfillRequest({
        requestId: params.requestId,
        responseCode: 200,
        body: Buffer.from(JSON.stringify({ name: 'Thomas' })).toString(
          'base64'
        ),
      });
    });
    
    // 符合以下模式的请求才会Fetch.requestPaused事件
    await Fetch.enable({
      patterns: [
        {
          urlPattern: '*/api/user',
          resourceType: 'XHR',
        },
      ],
    });
    
    // 允许跟踪网络，这时网络事件可以发送到客户端
    await Network.enable();
    
    await Page.enable();
    await Page.navigate({ url });
    // 等待页面加载
    await Page.loadEventFired();
  } catch (err) {
    console.error(err);
  }
}
// 我在本地3000端口起了服务，随便换一个网址也能看到页面各种资源的请求
intercept('https://gitee.com/projects/import/url');
