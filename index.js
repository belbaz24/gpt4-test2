import puppeteer from "puppeteer-core";
console.log("helloooo")

async function run () {
    let browser;

    try {
        const auth = 'username:password';

        browser = await puppeteer.connect({
            browserWSEndpoint:`wss://${auth}@host`
        });

        const page = await browser.newPage();
        page.setDefaultNavigationTimeout(2 * 60 * 1000);

        await page.goto('https://www.amazon.com/bestsellers');

        const selector = '.a-carousel'

        await page.waitForSelector(selector);
        const el = await page.$(selector);

        const text = await el.evaluate(e => e.innerHTML);

        console.log(text);

        return text;
    } catch (error) {
        console.error('scrape failed',error);
    }
    finally {
        await browser?.close();
    }
}

run()
