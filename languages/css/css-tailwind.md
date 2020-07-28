# CSS Tailwind

## Starting New Project

1. In a new directory, e.g., `my-tailwind-project`, run `npm init -y` to create a basic `package.json`
2. Install Tailwind with `npm install postcss-cli autoprefixer`
3. Run `npx tailwind init`, this creates an empty `tailwind.config.js`
4. Edit a new file at the root of the project called `postcss.config.js`, and add the following as its contents:

        module.exports = {
            plugins: [
                require('tailwindcss'),
                require('autoprefixer'),
            ]
        }

5. Create a new file at `css/tailwind.css`, add the following contents:

        @tailwind base;
        @tailwind components;
        @tailwind utilities;

6. Change the default `test` `scripts` entry in `package.json` to the following `build` entry:

        "build": "postcss css/tailwind.css -o public/build/tailwind.css"

7. Run `npm run build`
8. Edit a new HTML file at `public/index.html`, use a basic HTML template and add the following in the `<head>`:

        <link rel="stylesheet" href="/build/tailwind.css">

    And the following in the `<body>`:

        <h1>Hello World!</h1>  

9. Run a simple server from the public directory, e.g., `ruby -run -e httpd public -p 8000` and view the unstyled site at `localhost:8000`