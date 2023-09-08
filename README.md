# Pulumi Vercel OpenAI Chatbot Example

This example shows how to use [Pulumi](https://pulumi.com) to deploy a OpenAI Chatbot running on Vercel. The chatbot uses the [Vercel AI SDK](https://sdk.vercel.ai/docs) with [Next.js](https://nextjs.org/) and [OpenAI](https://openai.com) to create a ChatGPT-like AI-powered streaming chat bot.

## Deploy your own

Deploy the example using [Pulumi](https://pulumi.com):

[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/aaronkao/vercel-py-openai-chatbot/README.md)

## How to use

Clone this repo into your own GitHub repo. 

Enter the `pulumi` directory and initialize the Pulumi stack

```bash
cd pulumi
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

## Learn More

To learn more about OpenAI, Next.js, and the Vercel AI SDK take a look at the following resources:

- [Vercel AI SDK docs](https://sdk.vercel.ai/docs)
- [Vercel AI Playground](https://play.vercel.ai)
- [OpenAI Documentation](https://platform.openai.com/docs) - learn about OpenAI features and API.
- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
