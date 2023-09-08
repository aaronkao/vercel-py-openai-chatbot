# Pulumi Vercel OpenAI Chatbot Example

This example shows how to use [Pulumi](https://pulumi.com) to deploy a [OpenAI chatbot running on Vercel](https://github.com/vercel/ai/tree/main/examples/next-openai). The chatbot uses the [Vercel AI SDK](https://sdk.vercel.ai/docs) with [Next.js](https://nextjs.org/) and [OpenAI](https://openai.com) to create a ChatGPT-like AI-powered streaming chat bot.

[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/aaronkao/vercel-py-openai-chatbot/pulumi/)


## Prerequisites

- [Pulumi account and token](https://www.pulumi.com/docs/pulumi-cloud/accounts/#access-tokens)
- [Pulumi CLI](https://www.pulumi.com/docs/cli/)
- Vercel account and token
- OpenAI account and key
- GitHub integration installed in Vercel

## How to use

Clone or fork this repo into your own GitHub repo. 

Enter the `vercel-py-openai-chatbot/pulumi` directory and initialize the Pulumi stack

```bash
cd vercel-py-openai-chatbot/pulumi
pulumi stack init
```

You will need a Vercel API token and OpenAI API key. Set the configuration variables. 

```bash
pulumi config set --secret vercel:apiToken <VERCEL_API_TOKEN>
```

```bash
pulumi config set --secret openai_api_key <OPENAI_API_KEY>
```

```bash
pulumi config set git_repo <YOUR_GITHUB_REPO_PATH>
```

Execute the Pulumi program

```bash
pulumi up
```
To use your new chatbot, just follow the URL from the stack output in your browser. 

If you’d like to tear down all of these resources and delete your stack, run `pulumi destroy -rf --remove`. Otherwise, have fun playing around with your new chatbot and add whatever you like! 🙂


## Learn More

To learn more about Pulumi, OpenAI, and the Vercel AI SDK take a look at the following resources:

- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [Vercel AI SDK docs](https://sdk.vercel.ai/docs)
- [OpenAI Documentation](https://platform.openai.com/docs)