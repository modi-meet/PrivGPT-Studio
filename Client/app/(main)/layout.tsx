import type React from "react";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "../globals.css";
import ClientLayout from "@/components/client-layout";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "PrivGPT Studio",
  description:
    "Experience the future of AI conversations with both cloud-powered Gemini and privacy-focused local models",
  icons: {
    icon: "/logos/logo-icon-light.svg",

    other: [
      {
        rel: 'icon',
        url: '/logos/logo-icon-dark.svg',
        media: '(prefers-color-scheme: dark)', 
      },
    ],
  },
};

export default function RootLayout({children,}: {children: React.ReactNode;}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${inter.className} bg-white dark:bg-gray-900 text-black dark:text-white transition-colors duration-300`}
      >
          <ClientLayout>
            {children}
          </ClientLayout>
      </body>
    </html>
  );
}
